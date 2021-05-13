s = input()
#どうあがいても700円
v = 700
for i in s:
    #トッピング付けるときは+100円
    if(i=='o'):v += 100
print(v)
