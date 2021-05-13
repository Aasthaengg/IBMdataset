s=input()
k=int(input())

words=[]
for i in range(len(s)):words.append(s[i:])
words.sort()

record=[]
for i in words:
    for j in range(len(i)):
        word="".join(i[:j+1])
        if word not in record:
            record.append(word)
    if len(record)>=k:
        print(record[k-1]);exit()