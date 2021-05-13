import sys


if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    pref = [a[0]]
    cost = 10**18
    for  i in range(1,n):
        pref.append(pref[i-1] + a[i])
    for i in range(n):
        d1 = pref[i]
        d2 = pref[-1] - pref[i]
        cost = min(cost,abs(d1-d2))
    print(cost)