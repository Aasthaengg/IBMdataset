import sys

def atcoderB():
    
    global gamelis
    gamelis = []

    global alis
    global blis
    global clis
    alis = []
    blis = []
    clis = []


    for i in range(3):
        gamelis.append(input())
    alis = list(gamelis[0])
    blis = list(gamelis[1])
    clis = list(gamelis[2])
    funca()
    
def funca():
    global switchval
    if alis ==[]:
        print("A")
        sys.exit()
    switchval = alis[0]
    del alis[0]


    if switchval == "a":
        funca()
    if switchval == "b":
        funcb()
    if switchval == "c":
        funcc()

        
    
def funcb():
    global switchval
    if blis ==[]:
        print("B")
        sys.exit()
    switchval = blis[0]
    del blis[0]


    if switchval == "a":
        funca()
    if switchval == "b":
        funcb()
    if switchval == "c":
        funcc()
    else:
        print("B")

    
def funcc():
    global switchval
    if clis ==[]:
        print("C")
        sys.exit()
    switchval = clis[0]
    del clis[0]

    if switchval == "a":
        funca()
    if switchval == "b":
        funcb()
    if switchval == "c":
        funcc()
    else:
        print("C")


    
atcoderB()
