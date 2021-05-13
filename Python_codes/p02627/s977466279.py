A = input()

# 文字列において、全ての文字が大文字かどうか判定するには str.isupper() 
# 文字列において、全ての文字が小文字かどうか判定するには str.islower()

ans = ''
if A.isupper(): ans = 'A'
else: ans = 'a'

print(ans)