x,y,u,v=map(int,input().split())

p=u-x
q=v-y

S="U"*q+"R"*p+"D"*q
S+="L"*(p+1)+"U"*(q+1)+"R"*(p+1)+"D"+"R"+"D"*(q+1)+"L"*(p+1)+"U"
print(S)
