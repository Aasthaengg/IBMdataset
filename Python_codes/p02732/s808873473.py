from collections import Counter
 
def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    a_c = Counter(A)
    res = [int(v*(v-1)/2) for v in a_c.values()]
    cnt = sum(res)
    for a in A:
        ans = (cnt - (a_c[a]-1))
        print(ans)
 
if __name__ == '__main__':
    main()