def main():

    N, A, B = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort(reverse = True)

    if all(v[i] == v[0] for i in range(A)):
        ct = 0
        for i in range(N):
            if v[i] == v[0]:
                ct += 1
        cases = [1]
        for i in range(1, ct+1):
            cases.append(cases[-1]*(ct-i+1)//i)
        return v[0], sum(cases[A:(min(ct, B)+1)])
    else:
        i = 0
        tot = 0
        while i < A:
            tot += v[i]
            i += 1
        max_i = i
        ref = v[i-1]
        ct_used = 0
        for j in range(A):
            if v[j] == ref:
                ct_used += 1

        ct = 0
        for j in range(N):
            if v[j] == ref:
                ct += 1
        cases = 1
        for j in range(1, ct_used+1):
            cases = cases * (ct-j+1)//j
        return tot/max_i, cases

if __name__ == '__main__':
    output = main()
    for v in output:
        print(v)