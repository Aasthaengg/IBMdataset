al = list("abcdefghijklmnopqrstuvwxyz")

s = list(input())
for i in s:
    if i in al:
        del al[al.index(i)]
        
if len(al) == 0:
    print("None")
else:
    print(al[0])