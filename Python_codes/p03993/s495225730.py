def main():
    N=int(input())
    a=[int(_) for _ in input().split()]
    ans = 0
    for i,v in enumerate(a):
        if a[v-1] == i+1:
            ans += 1
    print(ans//2)

main()