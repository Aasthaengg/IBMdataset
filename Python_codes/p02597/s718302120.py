n=input()
i=list(input())
Wn=i.count("W")
print(Wn-i[(len(i)-Wn):].count("W"))