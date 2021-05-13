import sys
N = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))

result = 0
for index in range(N):
    if (index + 1) % 2 == 1:
        if a_list[index] % 2 == 1:
            result += 1
        
print(result)
        

