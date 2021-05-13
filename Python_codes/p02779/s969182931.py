x = int(input())
a = list(map(int, input().split()))
rslt = len(set(a))
print("YES" if x == rslt else "NO")