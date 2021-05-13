b=input()

print(b.translate(str.maketrans({"A":"T","T":"A","C":"G","G":"C"})))
