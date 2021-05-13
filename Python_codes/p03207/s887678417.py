l = sorted(list(int(input()) for _ in range(int(input()))), reverse=True)
print(sum(l) - l[0]//2)