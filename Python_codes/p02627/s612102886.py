import re

def alphabet():
    A = input()
    match = re.search(r"[a-z]",A)
    if match:
        print("a")
    else:
        print("A")
        
alphabet()