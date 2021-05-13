import sys
x = ""
x = sys.stdin.read()
# while True:
#     x += str(input())
#     t = time.time()

alist = list(x)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
aa = [0]*27
for num in alist:
    itr =0
    for alp in alphabet:
        if num == alp:
            aa[itr] += 1
            break;
        itr += 1
    itr = 0
    for ALP in ALPHABET:
        if num == ALP:
            aa[itr] += 1
            break;
        itr += 1
for i in range(26):
    print("{} : {}".format(alphabet[i], aa[i]))
