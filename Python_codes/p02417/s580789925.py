import sys

InputText = ""
while True:
    try:
        InputText += input().lower()
    except:
        break

alphabet = [chr(i) for i in range(97,97+26)]
count = [0 for i in range(26)]

for i in range(len(InputText)):
    for j in range(26):
        if InputText[i] == alphabet[j]:
            count[j] = int(count[j]) + 1


for i in range(26):
    print(alphabet[i],":",count[i])