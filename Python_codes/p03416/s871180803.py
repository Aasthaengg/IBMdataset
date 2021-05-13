A, B = map(int,input().split())

ans = 0
def palindrome(string): return 0 if string==string[::-1] else 1
for i in range(A, B+1):
    if palindrome(str(i)) == 0 :
        ans += 1

print(ans)