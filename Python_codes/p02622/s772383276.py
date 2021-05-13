A_word = str(input().rstrip())
B_word=  str(input().rstrip())

counter=0
for i in range(len(A_word)):
    if A_word[i]!=B_word[i]:
        counter+=1
print(counter)