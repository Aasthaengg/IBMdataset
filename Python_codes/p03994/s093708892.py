s=input()
k=int(input())

result=""
for ss in s:
    if ss=="a":
        result+="a"
    else:
        if k>= 123 - ord(ss):
            k-=123-ord(ss)
            result+="a"
        else:
            result+=ss


if k>0:
    k=k%(123-97)
    temp=chr((((ord(result[-1])-97)+k)%(123-97))+97)
    print(result[:-1]+temp)
else:
    print(result)

#print(ord("a")):97
#print(ord("b")):98
#print(ord("z")):122
#97ならそのまま
#aにするには123-ord()をすればいい