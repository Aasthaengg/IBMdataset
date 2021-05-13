def invert_letter(letter):
    inv_letter=""
    for c in letter:
        inv_letter+=c.upper() if c.islower() else c.lower()
    return inv_letter

def run():
    letter_list=list(input().split())
    
    inv_letter_list=[]
    
    for letter in letter_list:
        inv_letter=invert_letter(letter)
        inv_letter_list.append(inv_letter)
        
    
    line_letter=" ".join(inv_letter_list)
    
    print(line_letter)

run()
