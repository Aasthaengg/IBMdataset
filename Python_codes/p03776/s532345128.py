def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))
  
if __name__ == '__main__':
    from collections import Counter
    from math import factorial

    N,A,B = [int(i) for i in input().split()]
    V = [int(i) for i in input().split()]

    V.sort(reverse = True)
    max_list = [V[0:A]]
    max = sum(V[0:A]) / A

    for i in range(A+1,B+1):
        a = sum(V[0:i]) / i
        if max <= a:
            max_list.append(V[0:i])
            max = a
    print("{:.6f}".format(max))

    ans = 0
    for x in max_list:
        ans_sub = 1
        try:
            x = Counter(x).most_common()
        except TypeError:
            ans += ans_sub
            continue
        for i in range(len(x)):
            ans_sub *= comb(V.count(x[i][0]),x[i][1])
        ans += ans_sub
    print(int(ans))
