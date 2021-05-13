import re
s = input()
t = 'keyence'
#分割区間を固定して、先頭・末尾のマッチング
for i in range(len(t)+1):
    if s.startswith(t[:i+1]) and s.endswith(t[i+1:]):
        print('YES');exit()
print('NO')