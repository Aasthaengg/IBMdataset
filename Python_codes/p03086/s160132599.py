S=list(input())

acgt=["A","C","G","T"]

max_length = 0
length = 0
for word in S:
    if word in acgt:
        length+=1
    else:
        if length!=0:
            if max_length<length:
                max_length=length
            length=0
if length!=0:
    if max_length<length:
        max_length=length
print(max_length)
