W=input()
sentences=''
while True:
    try:
        sentence=input()
        sentences+=sentence
        if sentence=='END_OF_TEXT':
            break
        sentences+='\n'
    except EOFError:
        pass
answer_count=0
for l in sentences.split():
    if l.lower()==W:
        answer_count+=1
print(answer_count)
