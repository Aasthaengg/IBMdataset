def split(word): 
    return [char for char in word]  
inp=input()
list=split(inp)
count=0
x=1
str="Good"
for i in range(3):
    if list[count]==list[count+1]:
        str="Bad"
    count=count+1
print(str)