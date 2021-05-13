ans = 0
W = input().lower()
while(True):
    T = input()
    if(T == 'END_OF_TEXT'): break
    ans += T.lower().split().count(W)
print(ans)