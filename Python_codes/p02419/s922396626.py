target = input()
total_text = ""
while True:
 text = input()
 if(text=="END_OF_TEXT"):
  break
 total_text+=" "
 total_text+=text
#text2 = text.replace('\n',' ')
sentenceList = total_text.split()
count = 0
for word in sentenceList:
 if(word.lower() == target):
  count+=1
print(count)
