S = input()
ans = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if len(set(S))==26:
    print("None")
else:
    ans = set(ans) ^ set(S)
    print(sorted(ans)[0])