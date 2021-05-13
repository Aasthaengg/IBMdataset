O = input()
E = input()
txt = ""
if len(O) == len(E):
    for o,e in zip(O,E):
        txt += o + e
else:
    for o,e in zip(O,E):
        txt += o + e
    txt += O[-1]
print(txt)
    
