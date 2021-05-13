n= int(input())
s= input()
harf = int(len(s)/2)

if(s[:harf] == s[harf:]):
    print("Yes")
else:
    print("No")