s = input()
K = int(input())

ans = []

for i in s:
    if i == "a":
        ans.append("a")
        continue
    
    if ord(i) + K >= ord("z") + 1:
        ans.append("a")
        K -= ord("z") + 1 - ord(i)
    
    else:
        ans.append(i)
        


last = (K + ord(ans[-1]) - ord('a')) % 26
ans[-1] = chr(ord("a") + last)
print(''.join(ans))