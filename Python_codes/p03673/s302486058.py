n = int(input())
a = list(map(int, input().split()))
ans = [i for i in a[-1:: -2]] + [i for i in a[n%2: n: 2]]
print(" ".join(list(map(str, ans))))