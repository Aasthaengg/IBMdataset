def f():
    ans,c=0,0
    for t in input().replace('BC','y').replace('A','x'):
        if t=='y':ans+=c
        elif t=='x':c+=1
        else:c=0
    print(ans)
if __name__ == "__main__":
    f()