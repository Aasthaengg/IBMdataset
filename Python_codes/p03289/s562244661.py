s=input()
res="AC"
if s[0]!="A":res="WA"
elif s[2:-1].count("C")!=1:res="WA"
else:
    li=list(s)
    li.remove("A")
    li.remove("C")
    for i in li:
        if i!=i.lower():
            res="WA"
print(res)