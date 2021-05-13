word=input()
l=len(word)

if word[l-1]=="s":
  print("{}{}".format(word,"es"))
else:
  print("{}{}".format(word,"s"))