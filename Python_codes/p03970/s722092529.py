def main():
    s=input()
    xx="CODEFESTIVAL2016"
    z=0
    for i in range(0,len(xx)):
        if(s[i]!=xx[i]):
            z+=1
    print(z)

main()
