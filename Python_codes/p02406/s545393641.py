import sys
n = int(input())
sys.stdout.write(" ")
answer = []
for i in range(3, n + 1):
    if i%3 == 0:
        answer.append(i)
    elif '3' in str(i):
        answer.append(i)
print(*answer)