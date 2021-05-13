s=input()
li=list(s)

i=0
j=len(s)-1
answer=0

while i<j:
    if li[i]==li[j]:
        i+=1
        j-=1
    else:
        if li[i]!="x" and li[j]!="x":
            answer=-1
            break
        elif li[i]=="x" and li[j]!="x":
            answer+=1
            i+=1
        elif li[i]!="x" and li[j]=="x":
            answer+=1
            j-=1

print(answer)
