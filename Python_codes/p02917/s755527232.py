n = int(input())
b = list(map(int, input().split()))
a = [b[0],b[n-2]]
for i in range(n-2):
    a.append(min(b[i],b[i+1]))
print(sum(a))