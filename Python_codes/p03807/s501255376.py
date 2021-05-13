n = int(input())
a = [i for i in list(map(int, input().split())) if i % 2 == 1]
print("YES") if len(a)%2==0 else print("NO")