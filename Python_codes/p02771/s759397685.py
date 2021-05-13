ls = sorted(list(map(int,input().split())))
bool = 0 
if ls[0] == ls[1] and ls[1] != ls[2]:
    bool = 1 
elif ls[1] == ls[2] and ls[0] != ls[1]:
    bool = 1
elif ls[0] == ls[2] and ls[0] != ls[1]:
    bool = 1
if bool:
    print('Yes')
else:
    print('No')