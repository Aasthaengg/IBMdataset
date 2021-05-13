b=input()

enki={"A":"T","T":"A","G":"C","C":"G"}
ans=""
for i in b:
    ans+=enki[i]
print(ans)