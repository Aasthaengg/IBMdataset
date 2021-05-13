S = sorted(list(set(list(input()))))
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count = 0
for char in alfabet:
    if not(char in S):
        print(char)
        break
    count+=1
if count == 26:
    print("None")