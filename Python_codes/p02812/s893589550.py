n = int(input())
l = input()
cnt =  0
for i in range(n-2):
    if l[i:i+3] == 'ABC':
        cnt += 1
print(cnt)