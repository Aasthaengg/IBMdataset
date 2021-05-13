def gumoji(moji):
    if len(moji)%2==0:
        if moji[:int(len(moji)/2)]==moji[-int(len(moji)/2):]:
            return True
    return False

s = str(input())
s = s[:len(s)-1]
#print(s)
while len(s)>=2:
    if gumoji(s):
        break
    else:
        s = s[:len(s)-1]
    
print(len(s))
