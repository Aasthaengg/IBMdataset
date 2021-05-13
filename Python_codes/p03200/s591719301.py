string,ans,cnt = input(),0,1
length = len(string)
b_cnt = string.count("B")
for i in range(length):
    if string[i]=="B":
        ans+=length-b_cnt-i
        b_cnt-=1
print(ans)