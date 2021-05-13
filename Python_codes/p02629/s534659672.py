N = int(input())
ans = ['']

while N>0:
    N = N - 1
    ans.append(chr(int(N%26+1)+ord('a')-1))
    N = int(N/26)
    
ans.reverse()
print(''.join(ans))