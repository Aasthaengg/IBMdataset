S=input()
l = len(S)
#keyencexxxxx
if S[:7]=="keyence":
  print("YES")
#kxxxxxeyence
elif S[:1]=="k" and S[l-6:]=="eyence":
  print("YES")
#kexxxxxyence
elif S[:2]=="ke" and S[l-5:]=="yence":
  print("YES")
#keyxxxxxence
elif S[:3]=="key" and S[l-4:]=="ence":
  print("YES")
#keyexxxxxnce
elif S[:4]=="keye" and S[l-3:]=="nce":
  print("YES")
#keyenxxxxxce
elif S[:5]=="keyen" and S[l-2:]=="ce":
  print("YES")
#keyencxxxxxe
elif S[:6]=="keyenc" and S[l-1:]=="e":
  print("YES")
#xxxxxkeyence
elif S[l-7:]=="keyence":
  print("YES")
else:
  print("NO")
