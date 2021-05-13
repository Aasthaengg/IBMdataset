N = int(input())
A = [int(input()) for i in range(N)]
 
ok = 1
for a in A:
    if a % 2 == 1:
        ok = 0
print(["first", "second"][ok])