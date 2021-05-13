n = int(input())
s = input()
t = input()

tyouhuku = 0
for i in range(n):
    if s[i:]==t[:n-i]:
        tyouhuku = n-i
        break
        
print(max(n,2*n-tyouhuku))