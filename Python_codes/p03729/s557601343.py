def main():
    s = input().split()
    
    s1=list(s[0])
    s2=list(s[1])
    s3=list(s[2])
    a=len(s1)
    b=len(s2)
    c=len(s3)
    if(s1[a-1]==s2[0] and s2[b-1]==s3[0]):
        print("YES")
    else:
        print("NO")
    
main()