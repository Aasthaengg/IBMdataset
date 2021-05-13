#ABC052-B
n = int(input())
s = input()

result = [0]
cnt = 0
for i in range(n):
    if s[i] == 'I':
        cnt += 1
        result.append(cnt)
    else:
        cnt -= 1
        result.append(cnt)
        
print(max(result))